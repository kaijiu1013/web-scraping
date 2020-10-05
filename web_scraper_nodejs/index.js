const {Builder, By, Key, until} = require('selenium-webdriver');
 
let driver =   new Builder()
                .forBrowser('chrome')
                .build();


driver.get('https://track.cruxsystems.com/login')
      .then(function() {
        const elemEmail = driver.findElement(By.name('email'));
        const elemPassword = driver.findElement(By.name('password'));
        const elemSubmit = driver.findElement(By.tagName('input.button.right'))
        elemEmail.sendKeys('');
        elemPassword.sendKeys('');
        elemSubmit.click()
      })
      .then(function() {
        const elemSearchCon = driver.wait(until.elementLocated(By.tagName('textarea')));
        elemSearchCon.sendKeys('TGHU8666330', Key.RETURN)            
      })
      .then(async function(){
        async function test () {
           return await  driver.wait(until.elementLocated(By.tagName("div.flex-33")))   
           //driver.findElement(By.tagName('div.flex-33'))
          
        }

        // 处理 return await data
        // (async() => {
        //   // const elemConInfo = await test();
        //   // console.log(elemConInfo)
        //   // console.log("test is working")
        //  // elemConInfo.click()
        // })()

        // 将promise then里面的数据await之后传到下一个then里面
        const elemConInfo = await test();
        //console.log(elemConInfo)
        return elemConInfo
     })
     .then(function(elem) {
            elem.click()
            async function test2 () {
                return await driver.wait(until.elementLocated(By.tagName("div.details")))   
                //await driver.findElement(By.tagName('div.details'))
                //driver.wait(until.elementLocated(By.tagName("div.details")))   
            }
            (async() => {
              const test2Result = await test2();
              console.log(test2Result);
              console.log("test2 is working");
            })()
     })
     .catch(function(err) {
       console.log(err)
     })
     

