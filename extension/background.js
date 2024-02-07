chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if (request.contentScriptQuery == "queryFakeAccount") {
            var url = "https://trianglesnake.com/api/fade";
            fetch(url, {
                method: 'POST', // 或者GET，視您的API設計而定
                body: JSON.stringify(request.data),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(response => sendResponse({fake: response.fake}))
            .catch(error => console.log('Error:', error));
            return true;  // 必須返回true
        }
    }
);
