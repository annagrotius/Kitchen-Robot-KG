using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking; // allows us to use the UnityWebRequest class
using SimpleJSON;
using UnityEngine.UI;
using TMPro;
using System;

public class RESTGet : MonoBehaviour
{
    public List<GameObject> edibleObjects;
    public List<GameObject> nonEdibleObjects;
    public List<string> edibleList = new List<string>();
    public List<string> nonEdibleList = new List<string>();
    private Color originalColor;

    //public ToggleSelection toggleSelection;
    //private static string URL;
    //private static string itemName;
    //private static string fullURL;
    private readonly string baseQueryURL = "https://api.krr.triply.cc/queries/annadg/";
    public string queryURL;
    public bool queryUsage;
    public string data;
    public TextMeshProUGUI responseText;
    public Toggle edibleToggle;
    public Toggle usageToggle;

    void OnStart()
    {
        queryUsage = false;
        responseText.text = "hi";
    }


    // Determines which toggle option was selected and returns its base query
    public void ToggleSelected(string toggleName)
    {
        if (toggleName == "edible")
        // another if statement to check if the toggle is on
        {
            if (edibleToggle.isOn)
            {
                Debug.Log("should get edible items");
                queryURL = baseQueryURL + "edible-CQ-2/run";
                //Debug.Log(queryURL);
                StartCoroutine(GetData1(queryURL));
                queryUsage = false;
            }
        }

        else if (toggleName == "usages")
        {
            if (usageToggle.isOn)
            { 
                Debug.Log("should get usages for a given object");
            queryUsage = true;
            queryURL = baseQueryURL + "CQ-1-used-For/run?x=http%3A%2F%2Ftest.org%2Fbft.owl%23";
            //Debug.Log(queryURL);
            //https://api.krr.triply.cc/queries/annadg/CQ-1-Usages/run?x=http%3A%2F%2Ftest.org%2Fbft.owl%23apple
            }
        }
        else
        {
            queryUsage = false;
        }
    }

    IEnumerator GetData1(string uri)
    {
    Debug.Log("...Processing REST call...");

    using (UnityWebRequest webRequest = UnityWebRequest.Get(uri))
    {
        // Call/Request website and wait to finish
        yield return webRequest.SendWebRequest();
        if (webRequest.isNetworkError || webRequest.isHttpError)
        {
            Debug.Log("No response from website");
        }
        else
        {
            // get results from JSON              
            Debug.Log("Data retrieved!");
            JSONNode edibleData = JSON.Parse(webRequest.downloadHandler.text); // will return JSON response as a full text string

            // loop through edibleData response and check which items are edible 
            JSONNode edibleEntities = edibleData;
            string[] edibleEntityNames = new string[edibleEntities.Count];

            for (int i = 0; i < edibleData.Count; i++)
            {
                edibleEntityNames[i] = edibleEntities[i]["ke"];
            }

            // determine which instances are edible from the response
            // NOTE: could maybe change this to a separate function
            var bftInstances = new List<string>() { "table", "milk", "apple", "lemon", "refrigerator", "coffee", "croissant", "garnish", "hardboiled_egg", "scrambled_egg", "fried_egg", "orange_juice", "apple_juice", "butter", "salt_shaker", "pepper_shaker", "bread_basket", "egg_cup", "milk_pitcher", "fork", "knife", "spoon", "butter_knife", "glass", "teacup", "sauce_dish", "butter_dish", "bread_plate", "teacup_plate", "dining_table", "dining_chair", "cupboard" };

            foreach (var instance2 in bftInstances)
            {
                if (GameObject.Find(instance2))
                {
                    //foreach (var instance1 in edibleEntityNames)
                    for (int i = 0; i < edibleEntityNames.Length; i++)
                    {
                        //if (instance1.Contains(instance2))
                        if (edibleEntityNames[i].Contains(instance2))
                        {
                            var edibleObject = GameObject.Find(instance2);
                            edibleObjects.Add(edibleObject);
                            break;
                        }
                        else
                        {
                            if (i == edibleEntityNames.Length-1)
                            {
                                var nonEdibleObject = GameObject.Find(instance2);
                                nonEdibleObjects.Add(nonEdibleObject);
                            }
                            else
                            {
                                continue;
                            }                                
                        }
                    }
                }
            }

            // Set UI objects - i.e. activate edible and nonedible 
            // set edible objects to green
            Debug.Log("EDIBLE");
            foreach (GameObject obj in edibleObjects)
            {
                Debug.Log(obj.ToString());
                Component[] renderers = obj.GetComponentsInChildren(typeof(Renderer));
                foreach (Renderer childRenderer in renderers)
                {
                    childRenderer.material.color = Color.green;
                }
            }
            // set non-edible objects to red
            Debug.Log("NON-EDIBLE");
            foreach (GameObject obj in nonEdibleObjects)
            {
                Debug.Log(obj.ToString());
                Component[] renderers = obj.GetComponentsInChildren(typeof(Renderer));
                foreach (Renderer childRenderer in renderers)
                {
                    childRenderer.material.color = Color.red;
                }

            }
        }
      }
    }


    public IEnumerator GetData2(string uri, System.Action<string> callback)
    {
        using (UnityWebRequest webRequest = UnityWebRequest.Get(uri))
        {

        //UnityWebRequest webRequest = UnityWebRequest.Get(uri);
            // Call/Request website and wait to finish
            yield return webRequest.SendWebRequest();
            if (webRequest.isNetworkError || webRequest.isHttpError)
            {
                Debug.Log("No response from website");
            }
            else
            {
                //process web result             
                Debug.Log("Data retrieved!");
                callback(webRequest.downloadHandler.text);

                //string data = webRequest.downloadHandler.text;
                //JSONNode data = JSON.Parse(webRequest.downloadHandler.text);
                // Debug.Log(data);
                //yield return data;

                //JSONNode data = JSON.Parse(webRequest.downloadHandler.text);
                ////Debug.Log(data[0]["use"].Value);
                //JSONNode dataResponses = data;
                //string[] dataResponsesArray = new string[dataResponses.Count];

                //for (int i = 0; i < data.Count; i++)
                //{
                //    dataResponsesArray[i] = dataResponses[i]["use"];
                //}

                //// Set UI objects
                //string answer = "";
                //for (int i = 0; i < dataResponsesArray.Length; i++)
                //{
                //    answer += dataResponsesArray[i] + ", ";
                //}

                //Debug.Log(answer);
                ////return answer;
            }
      }
    }

    // new coroutine

}

