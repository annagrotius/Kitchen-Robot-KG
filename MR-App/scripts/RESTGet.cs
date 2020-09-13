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
    private readonly string baseQueryURL = "https://api.krr.triply.cc/queries/annadg/";
    public string queryURL;
    public string baseResponse;
    public bool queryUsage = false;
    public string data;
    public Toggle edibleToggle;
    public Toggle usageToggle;
    public Toggle locationToggle;
    public Toggle affordsToggle;
    public Toggle qualitiesToggle;


    // Determines which toggle option was selected and returns its base query
    public void ToggleSelected()
    {

        if (edibleToggle.isOn)
        {
            queryUsage = false;
            Debug.Log("should get edible items");
            queryURL = baseQueryURL + "edible-CQ-2/run";
            StartCoroutine(GetData1(queryURL));
            
        }
        else
        {
            SetColor(edibleObjects, Color.white);
            SetColor(nonEdibleObjects, Color.white);
            edibleList.Clear();
            nonEdibleList.Clear();
        }


        if (usageToggle.isOn)
        {
            Debug.Log("should get usages for a selected object");
            queryUsage = true;
            queryURL = baseQueryURL + "CQ-1-Usages/run?x=http%3A%2F%2Ftest.org%2Fbft.owl%23";
            baseResponse = "used for: ";
            //https://api.krr.triply.cc/queries/annadg/CQ-1-Usages/run?x=http%3A%2F%2Ftest.org%2Fbft.owl%23apple
        }
        else if (locationToggle.isOn)
        {
            Debug.Log("should get locations for a selected object");
            queryUsage = true;
            queryURL = baseQueryURL + "CQ-4-location/run?x=http%3A%2F%2Ftest.org%2Fbft.owl%23";
            baseResponse = "located at: ";
            //https://api.krr.triply.cc/queries/annadg/CQ-4-location/run?x=http%3A%2F%2Ftest.org%2Fbft.owl%23milk
        }
        else if (affordsToggle.isOn)
        {
            Debug.Log("should get affordances for a selected object");
            queryUsage = true;
            queryURL = baseQueryURL + "affords-new/run?ke=http%3A%2F%2Fapi.conceptnet.io%2Fc%2Fen%2F";
            baseResponse = "affords: ";
            //https://api.krr.triply.cc/queries/annadg/affords-new/run?ke=http%3A%2F%2Fapi.conceptnet.io%2Fc%2Fen%2Frefrigerator
        }
        else if (qualitiesToggle.isOn)
        {
            Debug.Log("should get qualities for a selected object");
            queryUsage = true;
            queryURL = baseQueryURL + "CQ-6-qualities-new/run?ke=http%3A%2F%2Fapi.conceptnet.io%2Fc%2Fen%2F";
            baseResponse = "qualities include: ";
            //https://api.krr.triply.cc/queries/annadg/CQ-6-qualities-new/run?ke=http%3A%2F%2Fapi.conceptnet.io%2Fc%2Fen%2Fmilk
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
                // process webrequest and get results from JSON              
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
                var bftInstances = new List<string>() { "table", "milk", "apple", "lemon", "refrigerator", "coffee", "croissant", "garnish", "hardboiled_egg", "scrambled_egg", "fried_egg", "orange_juice", "apple_juice", "butter", "salt_shaker", "pepper_shaker", "bread_basket", "egg_cup", "milk_pitcher", "fork", "knife", "spoon", "butter_knife", "glass", "teacup", "sauce_dish", "butter_dish", "bread_plate", "teacup_plate", "dining_table", "dining_chair", "cupboard" };

                foreach (var instance2 in bftInstances)
                {
                    if (GameObject.Find(instance2))
                    {
                        for (int i = 0; i < edibleEntityNames.Length; i++)
                        {
                            if (edibleEntityNames[i].Contains(instance2))
                            {
                                var edibleObject = GameObject.Find(instance2);
                                edibleObjects.Add(edibleObject);
                                break;
                            }
                            else
                            {
                                if (i == edibleEntityNames.Length - 1)
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

                // Set UI objects - i.e. add color to edible and nonedible 
                Debug.Log("EDIBLE");
                SetColor(edibleObjects, Color.green);
                Debug.Log("NON-EDIBLE");
                SetColor(nonEdibleObjects, Color.red);
            }
        }
    }


    public IEnumerator GetData2(string uri, System.Action<string> callback)
    {
        using (UnityWebRequest webRequest = UnityWebRequest.Get(uri))
        {
            yield return webRequest.SendWebRequest();
            if (webRequest.isNetworkError || webRequest.isHttpError)
            {
                Debug.Log("No response from website");
            }
            else
            {
                //process web request             
                Debug.Log("Data retrieved!");
                callback(webRequest.downloadHandler.text);
            }
        }
    }


    public void SetColor(List<GameObject> gameObjects, Color color)
    {
        foreach (GameObject obj in gameObjects)
        {
            var colorChoice = color;
            Component[] renderers = obj.GetComponentsInChildren(typeof(Renderer));
            foreach (Renderer childRenderer in renderers)
            {
                childRenderer.material.color = colorChoice;
            }
        }
    }
}

