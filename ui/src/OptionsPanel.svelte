<script lang="ts">
    import ProcessingParam from "./ProcessingParam.svelte"
    import type {ImageProcessingParams} from "./stores"
    import {imageProcessingParams, imageStore, processedImageStore} from "./stores"

    let image: string
    let params: ImageProcessingParams

    imageStore.subscribe(value => image = value)
    imageProcessingParams.subscribe(value => params = value)

    function updateParam(e: Event) {
        const input = e.currentTarget as HTMLInputElement
        const name = input.name

        imageProcessingParams.update(value => ({
            ...value,
            [name]: input.value,
        }))
    }

    const handleSubmit = async (e: Event) => {
        const formData = new FormData(e.target as HTMLFormElement)

        const data = {}
        for (let field of formData) {
            const [key, value] = field
            data[key] = value
        }
        console.log(data)

        const requestBody = {
            data: image,
            params,
        }
        console.log(requestBody)
        const response = await fetch("http://localhost:8000/process", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(requestBody),
        })
        // console.log(response)

        if (response.ok) {
            const body = await response.json()
            processedImageStore.set(body.data)
        }
    }
</script>

<div class="options-panel">
    <h1 class="header">Options</h1>
    <form class="content" on:submit|preventDefault={handleSubmit}>
        <ProcessingParam name="posterize_levels" label="Posterize" value="{params.posterize_levels}" min="1" max="20" updateParam="{updateParam}" />
        <ProcessingParam name="num_clusters" label="Clusters" value="{params.num_clusters}" min="1" max="20" updateParam="{updateParam}" />
        <ProcessingParam name="blur_ksize" label="Blur Size" value="{params.blur_ksize}" min="1" max="20" updateParam="{updateParam}" />
        <ProcessingParam name="min_area_threshold" label="Min Area Threshold" value="{params.min_area_threshold}" min="0" max="5000" step="100" updateParam="{updateParam}" />
        <ProcessingParam name="font_scale" label="Font Scale" value="{params.font_scale}" min="0.1" max="2.0" step="0.1" updateParam="{updateParam}" />
        <ProcessingParam name="font_thickness" label="Font Thickness" value="{params.font_thickness}" min="1" max="5" updateParam="{updateParam}" />
        <button class="process-button">Process</button>
    </form>
</div>

<style>
    .options-panel {
        @apply flex flex-col w-96 min-h-[16rem] bg-gray-800 border-2 border-gray-700 rounded;
    }

    .content {
        @apply flex flex-col py-2;
    }

    .header {
        @apply flex flex-row justify-center text-gray-300 bg-gray-700 p-2 rounded-t;
    }

    .process-button {
        @apply bg-gray-700 rounded p-1 w-1/2 self-center mt-5 mb-2 transition-colors duration-200 ease-in-out;
    }

    .process-button:hover {
        @apply bg-gray-600 text-gray-200;
    }
</style>
