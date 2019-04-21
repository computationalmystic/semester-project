## Calling the front end

`You have two options for where to call your endpoint on the frontend:`
- in your card file
- in your chart file
 
I would recommend creating your own chart file with the following skeleton:
```
<template>
  <div ref="holder" style="position: relative; z-index: 5">
    <div class="chart">
      <h3 style="text-align: center">{{ title }}</h3>
      <vega-lite :spec="spec" :data="values"></vega-lite>
      <p> {{ chart }} </p>
    </div>
  </div>
</template>


<script>
import { mapState } from 'vuex'
import AugurStats from 'AugurStats'

export default {
  props: ['source', 'citeUrl', 'citeText', 'title', 'disableRollingAverage', 'alwaysByDate', 'data'],
  data() {
    return {
      values: [],
    }
  },
  computed: {
    repo() {
      return this.$store.state.baseRepo
    },
    spec() {
        // IF YOU WANT TO CALL YOUR ENDPOINT IN THE CHART FILE, THIS IS WHERE/HOW YOU SHOULD DO IT:
      let repo = window.AugurAPI.Repo({ githubURL: this.repo })
      repo[this.source]().then((data) => {
        console.log("HERE", data)
        this.values = data
      })
      //FINISH CALLING ENDPOINT
      
      // THIS IS A SAMPLE 'spec', SPECS ARE WHAT CREATE THE VEGA-LITE FILE, 
      // YOU CAN PLAY WITH SAMPLE SPEC OF A LINE CHART AT: 
      // https://vega.github.io/editor/#/examples/vega-lite/line
      // AND SEE THE DATA THAT THEY ARE USING AT:
      // https://vega.github.io/vega-lite/data/stocks.csv
      let config = {
        "$schema": "https://vega.github.io/schema/vega-lite/v2.json",
        "width": 950,
        "height": 300,
        "mark": "line",
        "encoding": {
          "x": {
            "field": "date", "type": "temporal",
          },
          "y": {
            "field": "value","type": "quantitative",
          },
        }
      }
      return config
    }
  },
  methods: {
    //define any methods you may need here
    //you can call them anywhere with: this.methodName()
  }
}
</script>
```

` if you choose to call your endpoint in your card file (the file that is rendering your chart component), do it in your card file's 'created' lifecycle hook block. You can use a card file that already exists or create one from the following skeleton:`
```
<template>
  <section>
    <div style="display: inline-block;">
      <h2 style="display: inline-block; color: black !important">{{ $store.state.baseRepo }}</h2>
      <h2 style="display: inline-block;" class="repolisting" v-if="$store.state.comparedRepos.length > 0"> compared to: </h2>
      <h2 style="display: inline-block;" v-for="(repo, index) in $store.state.comparedRepos">
        <span v-bind:style="{ 'color': colors[index] }" :value="repo" class="repolisting"> {{ repo }} </span> 
      </h2>
    </div>
    <div class="row">
        // YOUR CHART COMPONENTS GO HERE, HERE ARE 2 EXAMPLES FROM 
        // GrowthMaturityDeclineCard.vue :
      <div class="col col-6">
        <dynamic-line-chart source="closedIssues"
                    title="Closed Issues / Week"
                    cite-url="https://github.com/augurlabs/wg-gmd/blob/master/activity-metrics/closed-issues.md"
                    cite-text="Issues Closed">
        </dynamic-line-chart>
      </div>

      <div class="col col-6">
        <dynamic-line-chart source="codeCommits"
                    title="Code Commits / Week"
                    cite-url="https://github.com/augurlabs/wg-gmd/blob/master/activity-metrics/commits.md"
                    cite-text="Commits"
                    :data="values['endpoint_name']"> <!-- IF YOU CHOOSE TO CALL YOUR ENDPOINT IN THE CARD FILE: this line is what is passing the data through the charts data 'prop' -->
        </dynamic-line-chart>
      </div>
      //END OF THE TWO EXAMPLES
      
    </div>

    <small>Data provided by <a href="http://ghtorrent.org/msr14.html">GHTorrent</a> <span class="ghtorrent-version"></span> and the <a href="https://developer.github.com/">GitHub API</a></small>
  </section>
</template>

<script>
//IMPORT YOUR CHART COMPONENTS
import BubbleChart from './charts/BubbleChart'
import StackedBarChart from './charts/StackedBarChart'
import DynamicLineChart from './charts/DynamicLineChart'

module.exports = {
  components: {
  //DEFINE THEM HERE SO THAT YOU CAN REFERENCE THEM
    BubbleChart,
    StackedBarChart,
    DynamicLineChart
  },
  data() {
    return {
      values: [],
      colors: ["#FF3647", "#4736FF","#3cb44b","#ffe119","#f58231","#911eb4","#42d4f4","#f032e6"]
    }
  },
  methods: {
    //define any methods you may need here
    //you can call them anywhere with: this.methodName()
  },
  created () {
      //THIS BLOCK EXECUTES WHENEVER THIS CARD FILE GETS RENDERED,
      // IF YOU WANT TO CALL YOUR ENDPOINT IN YOUR CARD FILE,
      // THIS IS WHERE/HOW YOU SHOULD DO IT:
      
      let repo = window.AugurAPI.Repo({ githubURL: this.repo })
      repo[this.source]().then((data) => {
        // IF YOU ARE CREATING YOUR OWN CHART FILE, SET THIS.VALUES LIKE THIS
        this.values['endpoint_name'] = data
        
        // IF YOU ARE USING THE DYNAMIC LINE CHART, SET IT LIKE THIS
        this.values['endpoint_name'][this.repo]['endpoint_name']
        // this is so that 'this.values['endpoint_name'] = ' something with the following format (this is how DynamicLineChart.vue wants the data to be formatted):
            /*
            {
            	repo_name: {
            		endpoint_name: {
            			[
            				{data}, {data}, {data}
            			]
            		}
            	}
            }
            */
      })
      //FINISH CALLING ENDPOINT
  }
};
</script>
```