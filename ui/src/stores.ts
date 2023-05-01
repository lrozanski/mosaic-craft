import {writable} from "svelte/store"

type TooltipStore = {
    visible: boolean
    text: string
    target: Element | null
    offset?: Offset
}

type Offset = {
    x?: number,
    y?: number
}

function createTooltip() {
    const {subscribe, set} = writable<TooltipStore>({
        visible: false,
        text: "",
        target: null,
    })

    return {
        subscribe,
        show: (tooltip: string, target: Element, offset?: Offset) => {
            set({
                visible: true,
                text: tooltip,
                target,
                offset,
            })
        },
        hide: () => {
            set({
                visible: false,
                text: "",
                target: null,
            })
        },
    }
}

export const tooltip = createTooltip()


type MainStore = {
    image: string | null // base64

}

export type ImageProcessingParams = {
    posterize_levels: number
    num_clusters: number
    blur_ksize: number
    min_area_threshold: number
    font_scale: number
    font_thickness: number
}

const defaultProcessingParams: ImageProcessingParams = {
    posterize_levels: 6,
    num_clusters: 5,
    blur_ksize: 3,
    min_area_threshold: 3000,
    font_scale: 0.7,
    font_thickness: 2,
}

export const imageStore = writable<string | null>(null)
export const processedImageStore = writable<string | null>(null)

export const imageProcessingParams = writable<ImageProcessingParams>(defaultProcessingParams)
export const processedImageAlphaStore = writable<number>(0.5)
