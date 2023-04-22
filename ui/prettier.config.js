module.exports =
    {
        arrowParens: "avoid",
        bracketSameLine: true,
        bracketSpacing: false,
        endOfLine: "lf",
        printWidth: 180,
        quoteProps: "as-needed",
        semi: false,
        singleQuote: false,
        tabWidth: 4,
        trailingComma: "es5",
        useTabs: false,
        plugins: [
            require("prettier-plugin-svelte"),
            require("prettier-plugin-tailwindcss"),
        ],
    }
