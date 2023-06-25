<template>
    <div>
        <md-card-header>
            <div class="md-title">{{documentContent.name}}</div>
            <div class="md-subhead">
                <a :href="documentContent.link"></a>
            </div>
        </md-card-header>
        
        <md-card-content>
            {{documentContent.summary}}
        </md-card-content>

        <md-card-actions>
            <md-button>
                Vote-Up
            </md-button>
            <md-button>
                Vote-Down
            </md-button>
        </md-card-actions>
    </div>
</template>

<script>
export default {
    props: {
        documentContent: Object
    }
}
</script>