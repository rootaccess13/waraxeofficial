module.exports = {
    plugins: [
        // 将css编译为适应于多版本浏览器
        require('autoprefixer'),
        // 压缩css代码
        require('cssnano')
    ]
}