const path = require('path');
const fs = require('fs');

module.exports = class ChangeVersion {
    apply(compiler) {
        compiler.hooks.emit.tap('ChangeVersion', ()=>{
            this.setDistPackageVersion(this.getVersion())
        })
    }

    getVersion() {
        const pkg = this.getPkg('/../package.json')
        return pkg.version;
    }

    setDistPackageVersion(version) {
        const pkg = this.getPkg('/../dist/package.json');
        pkg.version = version;
        fs.writeFileSync(path.join(__dirname, '/../dist/package.json'), JSON.stringify(pkg, null, 2))
    }

    getPkg(pkgPath) {
        let pkg = fs.readFileSync(path.join(__dirname, pkgPath));
        return JSON.parse(pkg);
    }
}