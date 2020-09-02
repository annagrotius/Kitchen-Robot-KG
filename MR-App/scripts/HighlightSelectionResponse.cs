using TMPro;
using UnityEngine;

internal class HighlightSelectionResponse : MonoBehaviour, ISelectionResponse
{
    //[SerializeField] public Material highlightMaterial;
    //[SerializeField] public Material defaultMaterial;
    public TextMeshProUGUI gameText;
    public RESTGet rest;
    //string answer;
    private static string itemName;
    private string URL;

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

            //if (itemName == "apple")
            //{
            //    //itemName = "this is example";
            //    var URL = rest.queryURL + itemName;
            //    Debug.Log(URL);
            //}
            //else if (itemName == "lemon")
            //{
            //    itemName = "another example";
            //}
            //else
            //{
            //    itemName = "None";
            //}
            //Debug.Log(answer);
        }
        //Debug.Log(selection.GetType);

        //return itemName;
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
