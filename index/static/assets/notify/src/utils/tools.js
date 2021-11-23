export function $(el, con) {
    return typeof el === 'string' ? (con || document).querySelector(el) : el || null;
}

// get only id
export function getElId(text) {
    return text + '-' + Number(Math.random().toString().substr(3, 4) + Date.now()).toString(36);
}