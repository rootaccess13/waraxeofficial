const {CleanWebpackPlugin} = require('clean-webpack-plugin');
const ChangeVersion = require("./plugins/changeVersion")
const path = require('path');

module.exports = {
    mode: 'production',
    entry: {
        notice: "./src/index.js"
    },
    output: {
        filename: "[name].min.js",
        path: __dirname + '/dist',
        library: 'Notice',
        libraryTarget: 'umd',
        libraryExport: "default"
    },
    module: {
        rules: [{
            test: /\.css$/,
            use: ['style-loader','css-loader','postcss-loader']
        }]
    },
    plugins: [
        new ChangeVersion(),   // 修改文件版本号
        new CleanWebpackPlugin({
            verbose: true,
            cleanOnceBeforeBuildPatterns: [
                `!${path.resolve(__dirname, 'package*')}`,
            ]
        })
    ]
}