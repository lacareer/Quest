const {DynamoDBClient, PutItemCommand} = require("@aws-sdk/client-dynamodb");
const client = new DynamoDBClient();

exports.handler = async message => {
  console.log(message);

  if (message.body) {
    let bookmark = JSON.parse(message.body);
    let params = {
      TableName: process.env.TABLE_NAME,
      Item: {
        id: { S: bookmark.id },
        url: { S: bookmark.url },
        name: { S: bookmark.name },
        description: { S: bookmark.description },
        username: { S: bookmark.username },
        shared: { BOOL: bookmark.shared }
      }
    };
    
    
    console.log(`Adding bookmark to table ${process.env.TABLE_NAME}`);
    const command = new PutItemCommand(params);
    await client.send(command);
    console.log(`New bookmark added to the inventory`);
  }

  return {
    statusCode: 200,
    headers: {"Access-Control-Allow-Origin": '*'},
    body: JSON.stringify({})
  };
}
