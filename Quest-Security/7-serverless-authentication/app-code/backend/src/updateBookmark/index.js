const {DynamoDBClient, PutItemCommand} = require("@aws-sdk/client-dynamodb");
const client = new DynamoDBClient();

exports.handler = async message => {
  console.log(message);

  if (message.body) {
    let bookmarkId = message.pathParameters.id
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

    console.log(`Updating bookmark ${bookmarkId} in table ${process.env.TABLE_NAME}`);
    const command = new PutItemCommand(params);
    await client.send(command);
    console.log(`Bookmark is updated with new data`);
  }

  return {
    statusCode: 200,
    headers: {"Access-Control-Allow-Origin": '*'},
    body: JSON.stringify({})
  };
}
