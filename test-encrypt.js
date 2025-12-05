const token = "yO9DSWAzOBGOQ189KUUB45dFNLhli05vtQtQPi5T";
const password = "204204";
const key = password.split("").reduce((a, b) => a + b.charCodeAt(0), 0);
const encrypted = Buffer.from(
  token.split("").map((c, i) => 
    String.fromCharCode(c.charCodeAt(0) ^ ((key + i) % 256))
  ).join("")
).toString("base64");
console.log(encrypted);
