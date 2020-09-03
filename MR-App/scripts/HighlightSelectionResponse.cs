using TMPro;
using UnityEngine;
using SimpleJSON;
using UnityEngine.Networking;

internal class HighlightSelectionResponse : MonoBehaviour, ISelectionResponse
{
    //[SerializeField] public Material highlightMaterial;
    //[SerializeField] public Material defaultMaterial;
    public TextMeshProUGUI gameText;
    public RESTGet rest;
    //string answer;
    private static string itemName;
    private string URL;
    //string recentData = "";
    string returnData;

    public void OnSelect(Transform selection)
    {
        // this method only works if a query toggle is checked
        if (rest.queryUsage == true)
        {
            //Debug.Log(selection.name.ToString());
            //answer = rest.selectionObject(selection.name.ToString());
            var itemName = selection.name.ToString(); // name of the gameobject
            var URL = rest.queryURL + itemName;
            Debug.Log(URL);

            // START COROUTINE!!
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
                string answer = "";
                for (int i = 0; i < dataResponsesArray.Length; i++)
                {
                    // regex the string
                    answer += dataResponsesArray[i] + ", ";
                }

                // this should go in coroutine
                var selectionRenderer = selection.GetComponent<Renderer>();
                if (selectionRenderer != null)
                {
                    //selectionRenderer.material = this.highlightMaterial;
                    // this.gameObject.GetComponent // change color
                    gameText.text = answer;
                }
                // gameText.text = answer;
            }));
        }

        // this should go in coroutine
        //var selectionRenderer = selection.GetComponent<Renderer>();
        //    if (selectionRenderer != null)
        //    {
        //        //selectionRenderer.material = this.highlightMaterial;
        //       // this.gameObject.GetComponent // change color
        //        gameText.text = itemName;
        //    }
    }

    public void OnDeselect(Transform selection)
    {
        var selectionRenderer = selection.GetComponent<Renderer>();
        if (selectionRenderer != null)
        {
            //selectionRenderer.material = this.defaultMaterial;
            gameText.text = "";
        }
    }
}
