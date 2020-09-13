using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// code based on https://www.youtube.com/watch?v=_yf5vzZ2sYE

public class SelectionManager : MonoBehaviour
{
    [SerializeField] private string selectableTag = "Selectable";

    private ISelectionResponse _selectionResponse;

    private Transform _selection;

    private void Awake()
    {
        _selectionResponse = GetComponent<ISelectionResponse>();
    }

    // Update object selection each frame
    private void Update()
    {
        //  deselection/selection response
        // first checking whether selection field is null
        if (_selection != null)
        {
            //var selection = _selection;
            _selectionResponse.OnDeselect(_selection);
            //Debug.Log("selected");
        }

        #region MyRegion
        // Creating a ray. variable that represents ray cast in the game. Mouse position is the input.
        var ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        //RaycastHit hit;

        // Selection determination: check if the  ray is colliding with an object
        _selection = null;
        if (Physics.Raycast(ray, out var hit))
        {
            // if object is hit is True
            var selection = hit.transform;
            if (selection.CompareTag(selectableTag))
            {
                _selection = selection;
            }
        } 
        #endregion

        // deselection/selection response
        if (_selection != null)
        {
            //var selection = _selection;
            _selectionResponse.OnSelect(_selection);
        }

    }

}
