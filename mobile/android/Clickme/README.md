
![frida-re2](https://github.com/Meshari-SA/CTF/assets/45703970/4d62112e-a861-4b2e-90ee-03239dd3bb43)



Firstly, we can extract the source code from an APK file using apktool.

```Shell
apktool d file.apk
```


open the ```/clickme/resources/AndroidManifest.xml``` to find the entry point of app 


![image](https://github.com/Meshari-SA/CTF/assets/45703970/d5943d0f-221e-4434-b916-bf002112f135)

Let's inspect the source code of ```/clickme/sources/com/example/clickme/MainActivity.java```

![image](https://github.com/Meshari-SA/CTF/assets/45703970/b0ca3915-97ec-472b-b9a2-b143280f61ad)


We found a native function called getFlag. The question is, what is a native function?


![image](https://github.com/Meshari-SA/CTF/assets/45703970/e80e628f-c7cb-4e1b-80df-ba2daad6bbd1)

![image](https://github.com/Meshari-SA/CTF/assets/45703970/6183c0fc-d7c7-43f2-90ef-97be4405f4b0)

Now we know that the  ```getFlag``` function come from Library called ```clickme``` 

![image](https://github.com/Meshari-SA/CTF/assets/45703970/4b7b1a73-ab66-42cb-bdad-bd77e9e0be9a)

We can find the library at ```/clickme/resources/lib/x86/``` named  ```libclickme.so```,so we know is C/C++ we can open with IDA or Ghidra to look inside it.
Just go to the exports and search for ```getFlag```

![image](https://github.com/Meshari-SA/CTF/assets/45703970/67ea9300-0f7d-49b0-b52d-cab3e9659d3e)

Press Alt+3 to display as pseudocode.

![image](https://github.com/Meshari-SA/CTF/assets/45703970/0ff62690-ae17-4852-8830-3905c6f7759e)

There's a lot of code here, so it will take some time. I just want to show you where we can find the getFlag function.

Let's go to hooking the function to get the value that ```getFlag``` provides to us.

I will be using Frida to hook functions and Genymotion as an Android emulator.

We will create a JavaScript API using [this documentation](https://frida.re/docs/javascript-api/#java) from Frida to hook into the functions. 

```js
Java.perform(function(){
    var app_clickme = Java.use("com.example.clickme.MainActivity");
    app_clickme.getFlagButtonClick.implementation = function(view){
        this.CLICKS.value = 99999999;  
        var returnValue  = this.getFlagButtonClick(view); // calls the original function.
        console.log(this.getFlag());  // print the value of getFlag() in cmd.
        return returnValue;
    }

});

```

after clicking the button, we obtain the flag.

![image](https://github.com/Meshari-SA/CTF/assets/45703970/9157815a-6c53-42df-884a-20514f2fb7e0)





# EXTRA

If we have a lot of buttons on the screen (e.g., 10,000 buttons and 10,000 functions) and we know that only one button is executing a function from 10,000 functions,
how can we determine which button is executing the a function when it is clicked ?
  


>[!NOTE]
>This is a challenge from NahamCon CTF 2022.
