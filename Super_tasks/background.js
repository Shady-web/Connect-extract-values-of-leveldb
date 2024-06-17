chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.local.set({key: "Hello, World!"}, function() {
      console.log("Value is set to 'Hello, World!'");
    });
  });
  
  chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action == "getValue") {
      chrome.storage.local.get(["key"], function(result) {
        sendResponse({value: result.key});
      });
      return true;
    }
  });
  