using UnityEngine;

internal interface ISelectionResponse
{
    string OnSelect(Transform selection);

    void OnDeselect(Transform selection);
}
