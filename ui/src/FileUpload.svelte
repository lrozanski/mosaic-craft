<script lang="ts">
    import Icon from "@iconify/svelte"
    import {imageStore} from "./stores"

    let form: HTMLFormElement | null = null
    let fileInput: HTMLInputElement | null = null

    const handleFileChange = async (e: Event) => {
        const file = (e.currentTarget as HTMLInputElement).files[0]

        if (!file) {
            return
        }
        imageStore.set(await readFile(file))
    }

    const readFile = (file: File): Promise<string> => new Promise((resolve) => {
        const reader = new FileReader()

        reader.onload = () => resolve(reader.result as string)
        reader.readAsDataURL(file)
    })
</script>

<div on:click={() => fileInput.click()}>
    <Icon icon="ic:outline-photo-size-select-actual" class="w-full h-full" />
    <form bind:this={form} class="hidden">
        <label for="file">Upload image:</label>
        <input id="file" type="file" name="file" accept=".jpg, .jpeg, .png" required bind:this={fileInput} on:change={handleFileChange}>
        <button type="submit">Upload</button>
    </form>
</div>

<style>
</style>
