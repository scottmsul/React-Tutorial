# Background

When building a large codebase from scratch, usually there's periods of growth interspersed with periods of consolidation.
In my case, I was building a moderately-sized Flask project whose front-end consisted of many interwoven html templates and vanilla JS scripts.
Due to the increasing size and complexity, I decided to invest in learning a framework, and React seemed like a good choice given its popularity and reputation.
This repo consists of my attempts to learn React and to integrate it into an existing Flask project.

# Learning React

In my experience, when confronting any new technology, a good "first step" is to walk through some of the tutorials in order to internalize the basics of that technology.
As with learning any new skill, the first step was to google "learn react reddit" and click the first result. This quickly  led me to the official docs at [react.dev/learn](https://react.dev/learn).

## Initial Friction

The official docs have a [tic-tac-toe tutorial](https://react.dev/learn/tutorial-tic-tac-toe), which was my first real foray into actually using React.
I became *extremely* frustrated with this tutorial at the time.
This tutorial relies heavily on a magic "run everything in the browser" tool at [codesandbox.io](https://codesandbox.io/), but to me this felt "cutesy" for someone trying to learn a serious tool and integrate it into a real live-running project.
There were instructions for how to run the tutorial locally:

![React Installation Instructions](Images/tic-tac-toe-local-install-instructions.png)

But following these instructions led to an error:

![First Local Install Error](Images/tic-tac-toe-local-install-error.png)

After some [googling](https://stackoverflow.com/questions/42640636/react-must-be-in-scope-when-using-jsx-react-react-in-jsx-scope) I changed `App.js` from this:

```
export default function Square() {
  return <button className="square">X</button>;
}
```

To this:

```
import React from "react";

export default function Square() {
  return <button className="square">X</button>;
}
```

Which compiled! But then the next step was to return two buttons:

```
export default function Square() {
    return (
        <>
            <button className="square">X</button>
            <button className="square">X</button>
        </>
    );
}
```

Which again failed:

![Second Local Install Error](Images/tic-tac-toe-local-install-error-2.png)

At this point all the google results were saying "you're using JS and need to be using JSX duhhh!!!" even though this is the *default* installation from *their* repository.
I finally said "fuck it" and used the stupid cutesy in-browser tool for the rest of the tutorial.
At some point even this broke and I had to re-fork the code from a later step to get it working again.
Hopefully the devs at React will fix the local install issues.
In hindsight the tutorial was quite good from a conceptual standpoint, but the install issues were very frustrating at the time.

## React

To put it in my own words, the main high-level motivation behind React is the ability to develop a front-end by nesting custom html-like entities called *components*.
Components are programmable, re-usable, and can even be passed variables from components higher up in the DOM tree.
Components return an object that maps to an embeddable HTML fragment.
Probably their most useful feature is the ability to seamlessly react to changes in state, hence the name *React*.
Components can even be given callback functions that update state in their parent components, called *hooks*.
Going by the tic-tac-toe example, a typical React project  might have immutable state variables defined higher in the Component tree, with hooks that update these state variables lower in the Component tree.
Note that "immutable" in this context refers to an existing value not changing state, however the state can always be updated to a new immutable value.
