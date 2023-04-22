<script lang="ts">
    import ProcessingParam from "./ProcessingParam.svelte"
    import type {ImageProcessingParams} from "./stores"
    import {imageProcessingParams} from "./stores"

    let params: ImageProcessingParams
    imageProcessingParams.subscribe(value => params = value)

    function handleSubmit(e: Event) {
        console.log(e)
    }

    function updateParam(e: Event) {
        const input = e.currentTarget as HTMLInputElement
        const name = input.name

        imageProcessingParams.update(value => ({
            ...value,
            [name]: input.value,
        }))
    }
</script>

<div class="options-panel">
    <h1 class="header">Options</h1>
    <form on:submit|preventDefault={handleSubmit}>
        <ProcessingParam name="posterize_levels" label="Posterize" value="{params.posterize_levels}" min="1" max="20" updateParam="{updateParam}" />
        <ProcessingParam name="num_clusters" label="Clusters" value="{params.num_clusters}" min="1" max="20" updateParam="{updateParam}" />
    </form>
</div>

<style>
    .options-panel {
        @apply flex flex-col w-72 min-h-[32rem] bg-gray-800 border-2 border-gray-700 rounded;
    }

    .header {
        @apply flex flex-row justify-center text-gray-300 bg-gray-700 p-2 rounded-t;
    }
</style>
