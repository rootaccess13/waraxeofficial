export default function getLoadingEl(type, color) {
    switch (type) {
        case 'cube_flip':
            return `<div class="notice-loading-cube-flip" style="background-color: ${color}"></div>`;
            break;
        case 'dots_zoom':
            return `<div class="notice-loading-dots-zoom">
                        <div class="notice-loading-dots-zoom1" style="background-color: ${color}"></div>
                        <div class="notice-loading-dots-zoom2" style="background-color: ${color}"></div>
                    </div>`;
            break;
        case 'line' :
            return `<div class="notice-loading-line">
                      <div class="notice-loading-line-rect1" style="background-color: ${color}"></div>
                      <div class="notice-loading-line-rect2" style="background-color: ${color}"></div>
                      <div class="notice-loading-line-rect3" style="background-color: ${color}"></div>
                      <div class="notice-loading-line-rect4" style="background-color: ${color}"></div>
                      <div class="notice-loading-line-rect5" style="background-color: ${color}"></div>
                    </div>`
            break;
        case 'dots_spin':
            return `<div class="notice-loading-spin-dots">
                      <div class="notice-loading-spin-dot1" style="background-color: ${color}"></div>
                      <div class="notice-loading-spin-dot2" style="background-color: ${color}"></div>
                    </div>`
            break;
        case 'dots' :
            return `<div class="notice-loading-dots">
                      <div class="notice-loading-dot1" style="background-color: ${color}"></div>
                      <div class="notice-loading-dot2" style="background-color: ${color}"></div>
                      <div style="background-color: ${color}"></div>
                    </div>`
            break;
        case 'cube_zoom' :
            return `<div class="notice-loading-cube-zoom">
                      <div class="notice-loading-cube-zoom-1" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-2" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-3" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-4" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-5" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-6" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-7" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-8" style="background-color: ${color}"></div>
                      <div class="notice-loading-cube-zoom-9" style="background-color: ${color}"></div>
                    </div>`
            break;
    }
}