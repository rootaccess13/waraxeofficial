import './style/index.css'
import {$, getElId} from "./utils/tools";
import getLoadingEl from "./utils/loading";
import getToastEl from "./utils/toast";

class Notice {
    showLoading(options) {
        typeof options !== 'object' || options === null ? options = {} : '';

        // set Default Value
        const type = options.type || 'line',
            color = options.color || '#ffffff',
            backgroundColor = options.backgroundColor || 'rgba(0,0,0,.6)',
            title = options.title || '',
            fontSize = !!(Number(options.fontSize)) ? Number(options.fontSize) : 16;

        // create Parent Element
        const container = document.createElement('div');
        container.setAttribute('class', 'notice-loading notice-flex-center notice-fixed-all-page');
        container.setAttribute('id', 'notice-loading');

        // get Loading Element
        const loadingEl = getLoadingEl(type, color);


        container.innerHTML = `
                <div class="notice-mask notice-fixed-all-page" style="background-color: ${backgroundColor}"></div>
                <div class="notice-flex-center notice-loading-main">
                ${loadingEl}
                    ${title ? `<p style="color:${color};font-size: ${fontSize + 'px'};">${title}</p>` : ''}
                </div>
            `;
        $('body').appendChild(container);
    }

    hideLoading() {
        const loadingEl = $('#notice-loading');
        if (loadingEl) {
            $('body').removeChild(loadingEl)
        }
    }

    showToast(options) {
        typeof options !== 'object' || options === null ? options = {} : '';

        const text = options.text;
        // if not text , cannot show toast
        if(!text) return ;

        // get screen width
        const isPhone = screen.width < 576;

        // set Default Value
        const typeStyles = {
            default: {icon: '', phoneIcon: '', color: '#909399', backgroundColor: '#f4f4f5'},
            success: {icon: '&#xe66b;', phoneIcon: '&#xe600;', color: '#67c23a', backgroundColor: '#f0f9eb'},
            error: {icon: '&#xe651;', phoneIcon: '&#xe640;', color: '#e6a23c', backgroundColor: '#fdf6ec'},
            info: {icon: '&#xe89e;', phoneIcon: '&#xea11;', color: '#909399', backgroundColor: '#f4f4f5'},
            warning: {icon: '&#xe65b;', phoneIcon: '&#xea0c;', color: '#f56c6c', backgroundColor: '#fef0f0'},
        }
        const type = options.type || 'default';
        const typeStyle = typeStyles[type] || typeStyles['default'];
        isPhone ? typeStyle.icon = typeStyle.phoneIcon : '';

        let autoClose = typeof options.autoClose === "boolean" ? options.autoClose : true;
        typeStyle.showClose = options.showClose || false;
        typeStyle.text = text;


        const toastElementId = getElId('notice-toast');

        // if isPhone
        if(isPhone) {
            typeStyle.icon = typeStyle.phoneIcon;
            autoClose = true;

            if($('#notice-toast')){
                $('#notice-toast').remove();
            }
        }

        // Determine if toast exists
        if ($('#notice-toast')) {
            // create Element
            const main = document.createElement('div');
            main.setAttribute('class', 'notice-toast-main');
            main.setAttribute('id', toastElementId);
            main.setAttribute('style', `background:${typeStyle.backgroundColor}`);
            main.innerHTML = getToastEl(toastElementId,typeStyle,isPhone);
            $('#notice-toast').appendChild(main);
        } else {
            // create Parent Element
            const container = document.createElement('div');
            container.setAttribute('class', 'notice-toast');
            container.setAttribute('id', 'notice-toast');
            container.innerHTML =
                ` <div class="notice-toast-main" id="${toastElementId}" 
                        style="background:${typeStyle.backgroundColor}">
                    ${getToastEl(toastElementId,typeStyle,isPhone)}
                </div> `;
            $('body').appendChild(container);
        }

        // show animation
        setTimeout(() => $(`#${toastElementId}`).classList.add('notice-toast-main-active'));

        // Turn off regularly
        if(autoClose){
            setTimeout(() => {
                const el = $(`#${toastElementId}`);
                if(el){
                    el.classList.remove('notice-toast-main-active');
                    setTimeout(() => el.remove(), 500);
                }
            }, 4000);
        }
    }
}

export default Notice;