# Dynamic configuration

## Objectifs

Use an external config file to allow modification after build.
This is needed in devops when you build vue.js project an put in container.
You need to change some js variable in function on where you deploy the container.

This example you the method describe in https://www.iditect.com/how-to/54004759.html

## Receipts


```bash
export PROJECT_PATH="../simple"

#copy the cfg dir to your projet
cp -r ./cfg $PROJECT_PATH/cfg
```


Add ithis line in your ```$PROJECT_PATH/public/index.html``` before the ```<div id="app"></div>```
```js
<script src="/cfg/settings.js"></script>
```

Add this in your ```$PROJECT_PATH/vue.config.js``` (create vue.config.js in it not exit)

```javascript
module.exports = {
  chainWebpack: config => {
    config.plugin("copy").tap(([pathConfigs]) => {
      pathConfigs.unshift({
        from: "cfg",
        to: "cfg"
      });
      return [pathConfigs]})
  },
  transpileDependencies: ["vuetify"]
};
```

Now you can use these, anywhere in you project, to retrive config value
```js
window.__env.captcha.key
window.__env.captcha.api.url
window.__env.captcha.api.user
```