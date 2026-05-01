import { getData } from "../../general/utils.js";

const storeData = getData(); //Full aggregated data concerning this store
console.log(storeData);

window.setTimeout(() => {
    const side_section = document.getElementById("side_section");
    const backgroundF = document.getElementById("not-full-data");
    const sectionSupport = document.getElementById("support");
    const infoOnSideContainer = document.getElementById("side-info");
    infoOnSideContainer.style.opacity = "1";
    sectionSupport.style.opacity = "1";
    backgroundF.style.boxShadow = "inset 0px 0px 1000px #000000";
    side_section.style.rotate = "10deg";
    side_section.style.left = "50%";
    side_section.style.boxShadow = "-50px 0px 1000px #000000";
}, 200);