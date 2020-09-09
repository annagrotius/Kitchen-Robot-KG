using TMPro;
using UnityEngine;
using SimpleJSON;
using System.Text.RegularExpressions;
using UnityEngine.Networking;
using System.Linq;
using System.Collections;

internal class LemonSelectionResponse : MonoBehaviour, ISelectionResponse
{
    public TextMeshProUGUI gameText;
    public GameObject textPanel;
    public RESTGet rest;
    private readonly string itemName;
    private readonly string URL;
    string returnData;
    public string answer;
    //public GameObject responsePanel;

    private void Start()
    {
        var itemName = this.name.ToString();
        // if itemName == "lemon"...
        var URL = rest.queryURL + itemName;
        Debug.Log(URL);
        // urlDefined = true;

        StartCoroutine(rest.GetData2(URL, (value) =>
        {
            returnData = value;
            JSONNode data = JSON.Parse(returnData);
            // Debug.Log(data);
            JSONNode dataResponses = data;
            string[] dataResponsesArray = new string[dataResponses.Count];

            for (int i = 0; i < dataResponses.Count; i++)
            {
                dataResponsesArray[i] = dataResponses[i]["ans"];
            }

            // Set UI objects
            string _answer;
            answer = "";
            for (int i = 0; i < dataResponsesArray.Length; i++)
            {
                // regex the string
                _answer = cleanResponse(dataResponsesArray[i]);
                answer += _answer + ", ";
            }
        }));

    }

    public void OnSelect(Transform selection)
    {
        // this method only works if a query toggle is checked
        if (rest.queryUsage == true)
        {
            //Debug.Log(selection.gameObject.GetComponentInChildren(typeof(TextMeshProUGUI)));
            //var itemName = selection.name.ToString(); // name of the gameobject
            //var URL = rest.queryURL + itemName;
            //Debug.Log(URL);
            //// urlDefined = true;

            //StartCoroutine(rest.GetData2(URL, (value) =>
            //{
            //    returnData = value;
            //    JSONNode data = JSON.Parse(returnData);
            //    // Debug.Log(data);
            //    JSONNode dataResponses = data;
            //    string[] dataResponsesArray = new string[dataResponses.Count];

            //    for (int i = 0; i < dataResponses.Count; i++)
            //    {
            //        dataResponsesArray[i] = dataResponses[i]["ans"];
            //    }

            //    // Set UI objects
            //    string _answer;
            //    answer = "";
            //    for (int i = 0; i < dataResponsesArray.Length; i++)
            //    {
            //        // regex the string
            //        _answer = cleanResponse(dataResponsesArray[i]);
            //        answer += _answer + ", ";
            //    }
            //}));

            Debug.Log(selection.ToString());
            // retrieves respective game object text panel
            Component textComponent = selection.gameObject.GetComponentInChildren(typeof(TextMeshProUGUI));
            gameText = textComponent.GetComponent<TextMeshProUGUI>();
            //Component panelComponent = selection.gameObject.GetComponentInChildren(typeof(GameObject));
            //textPanel = textComponent.GetComponent<GameObject>();
            gameText.enabled = true;
            // textPanel.SetActive(true);
            //if (answer == "")
            //{
            //    gameText.text = "Knowledge not available";
            //}
            //else
            //{
            gameText.text = answer;
            //    }
            //}

            //StopCoroutine("GetData2");
        }
    }



        public void OnDeselect(Transform selection)
        {
            gameText.text = "";
            gameText.enabled = false;
            //textPanel.SetActive(false);
            answer = "";
            //StopAllCoroutines();
        }


        //void ShowQueryResponse(Transform selection, string response)
        //{
        //    var info = Instantiate(responsePanel, selection.position, Quaternion.identity);

        //    if (response == "")
        //    {
        //        info.GetComponent<TextMeshPro>().text = "Knowledge not available";
        //    }
        //    else
        //    {
        //        info.GetComponent<TextMeshPro>().text = response;
        //    }

        //}


        public string cleanResponse(string response)
        {
            string pattern = @"/";
            string result = Regex.Split(response, pattern, RegexOptions.IgnoreCase).Last();
            if (result.Contains("_"))
            {
                string _result = Regex.Replace(result, "_", " ");
                return _result;
            }
            return result;
        }
}

