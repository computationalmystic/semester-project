## Augur Frontend

`Augur.js`
 - 'hub' of Vue creation and linking Vue to the application
- imports all frontend packages
- creates VueX store
-- store contains options for visualizations and miscellaneous things like the current tab
-- the store's state's values can be accessed from any component in the application. For example: ```this.$store.state.baseRepo```
-- these options can only be changed through what vue calls 'mutations', which are defined in this file and can be called from any component in the frontend. These mutations are the only way to change the store's state
-- example of mutation call from MainControls.vue: ```
        this.$store.commit('setVizOptions', {
          rawWeekly: e.target.checked
        })```

- processes route's data and updates the store accordingly on every route change
-- e.g. the user changes the route from a single to a double comparison, then Augur.js will update the store's state based on the route change
- attaches Vue router to Augur application (which is a Vue app)

----------------

`AugurAPI.js`
- anything related to endpoints on the frontend
- contains methods for creating batch requests
- this is where new endpoints get added (so the frontend has access)
-- example from DownloadedReposCard.vue of calling an endpoint:    
```
    window.AugurAPI.getDownloadedGitRepos().then((data) => {
        // data handler for what endpoint returns
        $(this.$el).find('.spinner').removeClass('loader')
        $(this.$el).find('.spinner').removeClass('relative')
        this.repos = window._.groupBy(data, 'project_name')
        this.projects = Object.keys(this.repos)
      })
```
----------------

`AugurCards.vue`
- base template for most but not all pages on the frontend (LoginForm and MetricsStatus card are examples of exceptions, see how routes are different in router.js)
- router-view tags act as slots where components can be inserted by `router.js`
-- i.e. router-view for the name 'header' is often sent the AugurHeader component
-- See how these 'slots' are defined as children of the AugurCards component in router.js (childrens' paths are added to the end of its parent's path): 
```
{path: '/single/:owner?/:repo', name: 'single', props: true, 
canReuse: false, component: AugurCards,
        children: [
          {
            path: "gmd",
            name: "gmd",
            components: {
              header: AugurHeader,
              tabs: Tabs,
              controls: MainControls,
              content: GrowthMaturityDeclineCard
            }
          }, 
            ...
        ]
```

----------------

`router.js`
- add routes by defining paths and the component(s) you want to render at that path, see above example
- be sure to import your component!!: ```import Demo from '../components/Demo.vue'```

----------------

`Rendering a component within another component's template`
- you need to import your inner component in your 'container' component's <script></script> section: ```import AugurHeader from './AugurHeader'```
- Vue translates a name like 'AugurHeader' to something like 'augur-header' to be used as a tag. Example from MetricsStatusCard.vue:
```
<template>
  <div class="is-table-container">
    <div class="fullwidth">
      <augur-header></augur-header>
    </div>
    ...
  </div>
</template
```

-------

`` The Vue docs is your friend. You can always message me (Gabe Heim) with questions too``
