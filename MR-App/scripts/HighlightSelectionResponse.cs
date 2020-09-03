using TMPro;
using UnityEngine;
using SimpleJSON;
using UnityEngine.Networking;

internal class HighlightSelectionResponse : MonoBehaviour, ISelectionResponse
{
    public TextMeshProUGUI gameText;
    public RESTGet rest;
    private readonly string itemName;
    private readonly string URL;
    string returnData;
    public string answer;

    public void OnSelect(Transform selection)
    {
        // this method only works if a query toggle is checked
        if (rest.queryUsage == true)
        {
            var itemName = selection.name.ToString(); // name of the gameobject
            var URL = rest.queryURL + itemName;
            Debug.Log(URL);

            StartCoroutine(rest.GetData2(URL, (value) =>
            {
                returnData = value;
                JSONNode data = JSON.Parse(returnData);
                // Debug.Log(data);
                JSONNode dataResponses = data;
                string[] dataResponsesArray = new string[dataResponses.Count];

                for (int i = 0; i < dataResponses.Count; i++)
                {
                    dataResponsesArray[i] = dataResponses[i]["use"];
                }

                // Set UI objects
                answer = "";
                for (int i = 0; i < dataResponsesArray.Length; i++)
                {
                    // regex the string
                    answer += dataResponsesArray[i] + ", ";
                }
            }));

            if (answer == "")
            {
                gameText.text = "Knowledge not available";
            }
            else
            {
                gameText.text = answer;
            }
        }
    }
    

    public void OnDeselect(Transform selection)
    {
        gameText.text = "";
    }
}
