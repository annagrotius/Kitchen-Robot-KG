using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ToggleSelection : MonoBehaviour
{
    // Toggle game objects
    public Toggle edibleToggle;
    public Toggle usageToggle;

    private readonly string baseQueryURL = "https://api.krr.triply.cc/queries/annadg/";
    public static string queryURL;


    //Checks active toggle
    public string ToggleSelected(string toggleName)
    {
        if (edibleToggle.isOn)
        {
            Debug.Log("should get edible items");
            queryURL = baseQueryURL + "edible-CQ-2/run";
            //Debug.Log(queryURL);
        }

        else if (usageToggle.isOn)
        {
            Debug.Log("should get usages for a given object");
            queryURL = baseQueryURL + "CQ-1-used-For/run?x=http%3A%2F%2Ftest.org%2Fbft.owl%23milk";
           // Debug.Log(queryURL);
        }
        else
        {
            queryURL = "Nothing selected";
        }

        return queryURL;

    }

}
