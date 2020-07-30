def handle(event, context):
    print(event.body,flush=True)
    return {
        "statusCode": 200,
        "body": ""
    }
