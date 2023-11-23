import json, boto3
#comment
client = boto3.client('dynamodb')
TableName = 'CRCVisitorCounterDB'

def lambda_handler(event, context):
    
    '''
    data = client.get_item(
        TableName='CRCVisitorCounterDB',
        Key = {
            'stat': {'S': 'view-count'}
        }
    )
    '''
    
    #data['Item']['Quantity']['N'] = str(int(data['Item']['Quantity']['N']) + 1)
    
    response = client.update_item(
        TableName='CRCVisitorCounterDB',
        Key = {
            'stat': {'S': 'view-count'}
        },
        UpdateExpression = 'ADD Quantity :inc',
        ExpressionAttributeValues = {":inc" : {"N": "1"}},
        ReturnValues = 'UPDATED_NEW'
        )
        
    value = response['Attributes']['Quantity']['N']
    
    return {      
            'statusCode': 200,
            'body': value}
