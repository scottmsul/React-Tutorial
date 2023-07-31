const {
  StrictMode
} = React;
const {
  createRoot
} = ReactDOM;
const root = createRoot(document.getElementById("root"));
root.render( /*#__PURE__*/React.createElement(StrictMode, null, /*#__PURE__*/React.createElement(Game, null)));