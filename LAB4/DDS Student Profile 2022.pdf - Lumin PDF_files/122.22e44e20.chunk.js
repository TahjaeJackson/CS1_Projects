(window.webpackJsonp=window.webpackJsonp||[]).push([[122],{"./src/lumin-components/ToolStylePopupLumin/index.js":function(e,t,o){"use strict";o.r(t);var n=o("./node_modules/react-onclickoutside/dist/react-onclickoutside.es.js"),s=o("./node_modules/react-redux/es/index.js"),l=o("./src/redux/actions/index.js"),a=o("./src/redux/selectors/index.js"),i=o("./node_modules/@babel/runtime/helpers/classCallCheck.js"),r=o.n(i),c=o("./node_modules/@babel/runtime/helpers/createClass.js"),u=o.n(c),p=o("./node_modules/@babel/runtime/helpers/assertThisInitialized.js"),d=o.n(p),m=o("./node_modules/@babel/runtime/helpers/inherits.js"),h=o.n(m),v=o("./node_modules/@babel/runtime/helpers/possibleConstructorReturn.js"),y=o.n(v),f=o("./node_modules/@babel/runtime/helpers/getPrototypeOf.js"),b=o.n(f),j=o("./node_modules/@babel/runtime/helpers/defineProperty.js"),E=o.n(j),T=o("./node_modules/react/index.js"),O=o.n(T),S=o("./node_modules/prop-types/index.js"),g=o.n(S),x=o("./src/lumin-components/StylePalette/index.js"),P=o("./src/lumin-components/MaterialPopper/index.js"),C=o("./src/helpers/device.js"),k=o("./src/constants/map.js"),D=o("./src/core/index.js");function w(e){var t=function(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}();return function(){var o,n=b()(e);if(t){var s=b()(this).constructor;o=Reflect.construct(n,arguments,s)}else o=n.apply(this,arguments);return y()(this,o)}}var N=function(e){h()(o,e);var t=w(o);function o(e){var n;return r()(this,o),n=t.call(this,e),E()(d()(n),"getAnchorEl",(function(){var e=n.props,t=e.toolButtonObjects,o=e.activeToolName,s=t[o]&&t[o].dataElement,l=document.querySelector("[data-element=".concat(s,"]"));n.setState({anchorEl:l})})),E()(d()(n),"handleClick",(function(e){Object(C.m)()&&e.target===e.currentTarget&&n.props.closeElement("toolStylePopup")})),E()(d()(n),"handleClickOutside",(function(e){var t=document.querySelector('[data-element="toolsOverlay"]');(null===t||void 0===t?void 0:t.contains(e.target))||n.props.closeElement("toolStylePopup")})),E()(d()(n),"handleStyleChange",(function(e,t){var o=n.props.activeToolName;D.default.getTool(o).setStyles(E()({},e,t))})),n.popup=O.a.createRef(),n.state={anchorEl:null},n}return u()(o,[{key:"componentDidMount",value:function(){window.addEventListener("resize",this.close)}},{key:"componentDidUpdate",value:function(e){e.isOpen||!this.props.isOpen||this.props.isDisabled||(this.props.closeElements(["viewControlsOverlay","menuOverlay","signatureOverlay","zoomOverlay","redactionOverlay"]),this.getAnchorEl()),e.activeToolName!==this.props.activeToolName&&!this.props.isDisabled&&"AnnotationEdit"!==this.props.activeToolName&&this.getAnchorEl()}},{key:"componentWillUnmount",value:function(){window.removeEventListener("resize",this.close)}},{key:"render",value:function(){var e=this.state.anchorEl,t=this.props,o=t.isDisabled,n=t.activeToolName,s=t.activeToolStyle,l=t.isOpen,a=t.closeElement,i="AnnotationCreateFreeText"===n,r=Object(k.e)(n),c="AnnotationCreateStamp"===n;return o||void 0===l||!e?null:O.a.createElement(P.a,{open:l,anchorEl:e,handleClose:function(t){e.contains(t.target)||a("toolStylePopup")}},O.a.createElement("div",{className:"ToolStylePopupLumin","data-element":"annotationPopup"},O.a.createElement(x.a,{key:n,colorMapKey:r,style:s,isFreeText:i,hideDivider:c,onStyleChange:this.handleStyleChange})))}}]),o}(O.a.PureComponent);N.propTypes={activeToolName:g.a.string,activeToolStyle:g.a.object,isDisabled:g.a.bool,isOpen:g.a.bool,toolButtonObjects:g.a.object.isRequired,closeElement:g.a.func.isRequired,closeElements:g.a.func.isRequired},N.defaultProps={activeToolName:"",activeToolStyle:{},isDisabled:!1,isOpen:!1};var _=N,R={closeElement:l.a.closeElement,closeElements:l.a.closeElements};t.default=Object(s.c)((function(e){return{activeToolName:a.a.getActiveToolName(e),activeToolStyle:a.a.getActiveToolStyles(e),isDisabled:a.a.isElementDisabled(e,"toolStylePopup"),isOpen:a.a.isElementOpen(e,"toolStylePopup"),toolButtonObjects:a.a.getToolButtonObjects(e)}}),R)(Object(n.a)(_))}}]);