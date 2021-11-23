export default function getToastEl(id, {color,icon,showClose,text},isPhone) {
    return ` <div class="notice-toast-container">
                    ${icon ? `<i class="notice-iconfont notice-toast-icon" style="color: ${color}">${icon}</i>` : ''}
                    <p class="notice-toast-text ${isPhone && !icon  ? 'notice-toast-truncate-second' : ''}" style="color: ${color}; max-width: ${showClose ? 'calc(80vw - 125px)' : 'calc(80vw - 95px)'};">${text}</p> 
                </div>
                ${  showClose ?
        `<i class="notice-iconfont notice-close-icon"
                       onclick="
                            document.getElementById('${id}').classList.remove('notice-toast-main-active');
                            setTimeout(() => document.getElementById('${id}').remove(), 500);">
                        &#xe73e;
                    </i>`  : ''
    }`
}