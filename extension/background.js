chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "fetchData") {
      fetch(request.url)
          .then(response => response.text())
          .then(data => {
              console.log(data); // 在控制台中打印接收到的數據
              sendResponse({ success: true, data: data }); // 發送響應
          })
          .catch(error => {
              console.error('Error fetching data:', error); // 打印錯誤信息
              sendResponse({ success: false, error: error.message }); // 發送錯誤響應
          });

      return true;  // 保持消息通道開放以進行異步響應
  }
});