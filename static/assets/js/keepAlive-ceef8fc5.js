import{ak as r,al as h,am as p}from"./index-ad80de0e.js";const u=r({id:"geeker-tabs",state:()=>({tabsMenuList:[]}),actions:{async addTabs(e){this.tabsMenuList.every(s=>s.path!==e.path)&&this.tabsMenuList.push(e)},async removeTabs(e,s=!0){const t=this.tabsMenuList;s&&t.forEach((a,i)=>{if(a.path!==e)return;const n=t[i+1]||t[i-1];n&&h.push(n.path)}),this.tabsMenuList=t.filter(a=>a.path!==e)},async closeMultipleTab(e){this.tabsMenuList=this.tabsMenuList.filter(s=>s.path===e||!s.close)},async setTabs(e){this.tabsMenuList=e},async setTabsTitle(e){const s=location.hash.substring(1);this.tabsMenuList.forEach(t=>{t.path==s&&(t.title=e)})}},persist:p("geeker-tabs")}),o=r({id:"geeker-keepAlive",state:()=>({keepAliveName:[]}),actions:{async addKeepAliveName(e){!this.keepAliveName.includes(e)&&this.keepAliveName.push(e)},async removeKeepAliveName(e){this.keepAliveName=this.keepAliveName.filter(s=>s!==e)},async setKeepAliveName(e=[]){this.keepAliveName=e}}});export{o as a,u};