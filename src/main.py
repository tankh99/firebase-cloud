from firebase_functions import firestore_fn, https_fn, options
from firebase_admin import initialize_app, firestore
import google.cloud.firestore


region = 'asia-southeast1'

@https_fn.on_request(region=region)
def addmessage(req: https_fn.Request) -> https_fn.Response:
    original = req.args.get("text")
    if original is None:
        return https_fn.Response("No text received", status=400)
    
    firestore_client: google.cloud.firestore.Client = firestore.client()
    _, doc_ref= firestore_client.collection("messages").add({"original": original})
    return https_fn.Response(f"Successfully added message with id {doc_ref.id}")

@firestore_fn.on_document_created(document='messages/{pushId}', region=region)
def make_uppercase(event: firestore_fn.Event[firestore_fn.DocumentSnapshot | None]) -> None:
    if event.data is None:
        return
    try:
        original = event.data.get("original")
    except:
        
        return

    print(f"Uppercasing '{original}'")
    upper = original.upper()
    event.data.reference.update({"uppercase": upper})
    
app = initialize_app()