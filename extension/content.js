//post blck -> #barcelona-page-layout > div > div > div.xb57i2i.x1q594ok.x5lxg6s.x1ja2u2z.x1pq812k.x1rohswg.xfk6m8.x1yqm8si.xjx87ck.x1l7klhg.xs83m0k.x2lwn1j.xx8ngbg.xwo3gff.x1oyok0e.x1odjw0f.x1n2onr6.xq1qtft.xz401s1.x195bbgf.x3ir7cq.x1l19134.x1m0igow.x1ejq31n.xu3j5b3.x1q0q8m5.x26u7qi.x13lgxp2.x168nmei.xt8cgyo.xj515ic.x1co6499.x2j4hbs.x1ma7e2m.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x6ikm8r.xy5w88m.xh8yej3.xbwb3hm.x1x3vcui.x19xvnzb.x1y4ox9t.xev1tu8.xpr2fh2.xgzc8be.x1y1aw1k > div.x78zum5.xdt5ytf.x1iyjqo2.x1n2onr6 > div.x1c1b4dv.x13dflua.x11xpdln > div > div.x78zum5.xdt5ytf.x1iyjqo2.x1n2onr6 > div
//username -> div > div > div > div > div.xqcrz7y.x1xdureb.x1agbcgv > div > div.x7a106z.xamitd3.x78zum5.xdt5ytf.xlqzeqv > div > span.x6s0dn4.x78zum5.x1q0g3np > div > div > a
// img to inner -> x1pha0wt xmixu3c x78zum5 xdod15v
var userlen = 2;

function fetchData(url) {
    return new Promise((resolve, reject) => {
        chrome.runtime.sendMessage({action: "fetchData", url:url}, function(response) {
            if (response.success){
                resolve(response.data);
            }
            else {
                console.error(response.error);
                reject(response.error);
            }
        });
    })
}

async function isMalicious(username) {
    var api_url = "http://localhost/fade?username="+username;
    return fetchData(api_url).then(result => {
        if (result === "true") return true;
        else if (result === "false") return false;
        else throw new Error(username + " Error: "+result);
    });
}

const whitelist = /[^a-z\d._]+$/i;

const observer = new MutationObserver((mutations) => {
    if (mutations == undefined) return;
    var usernames = document.getElementsByClassName("x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xjohtrz x1s688f xp07o12 x1yc453h");
    
    if (usernames.length <= userlen)return;

    for (let username of Array.from(usernames).slice(userlen)) {
        
        if (username.textContent === "為你推薦") continue;
        //debugger;
        isMalicious(username.textContent).then(result => {
            console.log(username.textContent, result);
            if (result){
                username.innerText += "✅";
            }
            else {
                username.innerText += "❌";
            }
        })
        
    }
    userlen = usernames.length;
});

const config = { childList: true, subtree: true };

// 啟動監視
observer.observe(document.body, config);
