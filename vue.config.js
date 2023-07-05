const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  // css: {
  //   loaderOptions: {
  //     sass: {
  //       prependData: `
  //         @import "@/styles/_variables.scss";
  //         $primary-color: #FF0000;
  //         $accent-color: #00FF00;
  //       `
  //     }
  //   }
  // }
})
