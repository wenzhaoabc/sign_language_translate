import{a as T}from"./news-a9373ddc.js";import{d as g,i,j as V,r as n,o as l,c as m,a as t,F as v,f as L,h as p,w as _,J as N,b as f,t as d,e as b}from"./index-ad80de0e.js";import{_ as B}from"./_plugin-vue_export-helper-c27b6911.js";const I={class:"card"},M={class:"item-right"},H={class:"sub-text"},A={class:"mle"},D=["innerHTML"],E=g({name:"newsIndex"}),F=g({...E,setup(j){const s=i();V(async()=>{const{data:o}=await T();s.value=o});const x=o=>{const a=document.createElement("div");return a.innerHTML=o,a.innerText},c=i(!1),r=i(0);return(o,a)=>{var u;const h=n("el-image"),w=n("el-button"),y=n("el-card"),k=n("el-dialog");return l(),m(v,null,[t("div",I,[(l(!0),m(v,null,L(s.value,(e,C)=>(l(),p(y,{class:"news-item",shadow:"hover",key:e.id},{default:_(()=>[f(h,{class:"news-cover",src:e.image,"preview-src-list":[e.image],"preview-teleported":""},null,8,["src","preview-src-list"]),t("div",M,[t("h3",null,d(e.title),1),t("span",H,d(e.author+" "+e.created),1),f(w,{style:{float:"right"},size:"small",type:"text",onClick:z=>{r.value=C,c.value=!0}},{default:_(()=>[b("详情")]),_:2},1032,["onClick"]),t("p",A,d(x(e.content)),1)])]),_:2},1024))),128))]),(u=s.value)!=null&&u.length?(l(),p(k,{key:0,"model-value":c.value,"onUpdate:modelValue":a[0]||(a[0]=e=>c.value=e),title:s.value[r.value].title},{default:_(()=>[t("div",{innerHTML:s.value[r.value].content},null,8,D)]),_:1},8,["model-value","title"])):N("",!0)],64)}}});const U=B(F,[["__scopeId","data-v-401e4854"]]);export{U as default};