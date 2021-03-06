﻿using TMPro;
using UnityEngine;
using SimpleJSON;
using System.Text.RegularExpressions;
using System.Linq;
using UnityEngine.UI;

internal class HighlightSelectionResponse : MonoBehaviour, ISelectionResponse
{
    public TextMeshProUGUI gameText;
    public Image textPanel;
    public RESTGet rest;
    private readonly string itemName;
    private readonly string URL;
    string returnData;
    public string answer;
    bool enableSelection = false;
    int counter = 0;

    private void Update()
    {
        BeginRestCall(rest.queryUsage);
    }


    public void BeginRestCall(bool querySelected)
    {
        if (querySelected == true && counter < 1 )
        {
            enableSelection = true;
            var itemName = this.name.ToString();
            var URL = rest.queryURL + itemName;
            Debug.Log(URL);
            
            // calls coroutine from RESTGet
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

                string _answer;
                answer = "";
                for (int i = 0; i < dataResponsesArray.Length; i++)
                {
                    // regex the string
                    _answer = cleanResponse(dataResponsesArray[i]);

                    if (i == dataResponsesArray.Length - 1)
                    {
                        answer += _answer;
                    }
                    else
                    {
                        answer += _answer + ", ";
                    }
                }
            }));

            ++counter;
        }
        else
        {
            rest.queryURL = "";
            rest.queryUsage = false;
            counter = 0;
        }
    }


    public void OnSelect(Transform selection)
    {
        // this method only works if a query toggle is checked
        if (enableSelection == true)
        {
            // retrieves respective game object text panel ans display query information
            Component textComponent = selection.gameObject.GetComponentInChildren(typeof(TextMeshProUGUI));
            gameText = textComponent.GetComponent<TextMeshProUGUI>();
            string response = selection.gameObject.GetComponent<HighlightSelectionResponse>().answer;
            Component canvas = selection.gameObject.GetComponentInChildren(typeof(Canvas));
            Component panelCompnent = canvas.GetComponentInChildren(typeof(Image));
            textPanel = panelCompnent.GetComponent<Image>();
            if (response == "")
            {
                gameText.text = "Knowledge not available";
            }
            else
            {
                gameText.text = selection.gameObject.name + " " + rest.baseResponse + response;
            }

            gameText.enabled = true;
            textPanel.enabled = true;
        }
    }


    public void OnDeselect(Transform selection)
    {
        gameText.text = "";
        gameText.enabled = false;
        textPanel.enabled = false;
    }


    // processes the text retrieved from the coroutine
    public string cleanResponse(string response)
    {
        string pattern; 
        string pattern1 = @"/";
        string pattern2 = @"#";
        if (response.Contains('#'))
        {
            pattern = pattern2;
        }
        else
        {
            pattern = pattern1;
        }

        string result = Regex.Split(response, pattern, RegexOptions.IgnoreCase).Last();
        if (result.Contains("_"))
        {
            string _result = Regex.Replace(result, "_", " ");
            return _result;
        }
        return result;
    }
}

