(window.webpackJsonp=window.webpackJsonp||[]).push([[119],{"./src/lumin-components/SignInUseCommentModal/index.js":function(e,n,a){"use strict";a.r(n);var t=a("./node_modules/@babel/runtime/helpers/slicedToArray.js"),s=a.n(t),o=a("./node_modules/react/index.js"),c=a.n(o),i=a("./node_modules/react-redux/es/index.js"),r=a("./node_modules/react-router-dom/esm/react-router-dom.js"),m=a("./src/lumin-components/Icomoon/index.js"),l=a("./src/lumin-components/ButtonMaterial/index.js"),d=a("./src/redux/actions/index.js"),u=a("./src/redux/selectors/index.js"),p=a("./node_modules/classnames/index.js"),j=a.n(p);var g=function(){var e=Object(i.e)(),n=Object(i.f)((function(e){return[u.a.isElementOpen(e,"signInUseCommentModal")]})),a=s()(n,1)[0],t=function(){e(d.a.closeElement("signInUseCommentModal"))};return c.a.createElement("div",{className:j()({Modal:!0,SignInUseCommentModal:!0,open:a,closed:!a}),"data-element":"signInUseCommentModal",onClick:t},c.a.createElement("div",{className:"container",onClick:function(e){return e.stopPropagation()}},c.a.createElement(m.a,{className:"comment container-icon",size:48}),c.a.createElement("div",{className:"title"},"Sign in required"),c.a.createElement("div",{className:"message"},"Sign in to use Comment feature."),c.a.createElement("div",{className:"button-wrapper"},c.a.createElement(l.a,{type:"button",className:"secondary",onClick:t},"Cancel"),c.a.createElement(l.a,{type:"button",className:"primary"},c.a.createElement(r.a,{to:"/authentication/signin",replace:!0},"Sign In Now")))))};n.default=g}}]);