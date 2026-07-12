from documents.models import Document
from langchain.tools import tool
from langchain_core.runnables import RunnableConfig

@tool
def list_documents(config: RunnableConfig):
    """list the most recent 5 documents for the current user"""
    #print(config)

    limit = 5
    configurable = config.get("configurable") or config.get("metadata")
    user_id = configurable.get("user_id")
    query_set_list = []
    #serialize the query set to a list of dictionaries
    query_set = Document.objects.filter(active=True, owner_id=user_id).order_by("-created_at")
    for qry in query_set[:limit]:
        query_set_list.append({
            "id": qry.id,
            "name": qry.title
        })
        
    return query_set_list        

@tool
def get_document_by_id(document_id:int, config: RunnableConfig):
    """ return a document by id"""
    configurable = config.get("configurable") or config.get("metadata")
    user_id = configurable.get("user_id")
    print("user_id: ", user_id)
    if user_id is None:
        raise Exception("Invalid user_id: {}".format(user_id))
    try:
        query_set = Document.objects.get(active=True, id=document_id, owner_id=user_id)
    except Document.DoesNotExist:
        return "Error: Document with id {} does not exist".format(document_id)
    except:
        raise Exception("Error: Unable to retrieve document with id {}".format(document_id))
    else:
        return {
            "id": query_set.id,
            "name": query_set.title
            }
    
tools = [list_documents, get_document_by_id]