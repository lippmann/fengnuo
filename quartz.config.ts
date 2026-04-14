import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "冯诺",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: false,
    analytics: {
      provider: "plausible",
    },
    locale: "zh-CN",
    // 待填写真实域名，例如 fengnuo.com
    baseUrl: "YOUR_DOMAIN_HERE",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Noto Serif SC",
        body: "Noto Serif SC",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#F5F0E8",
          lightgray: "#E0D8CE",
          gray: "#B0A496",
          darkgray: "#6A6258",
          dark: "#2C2C2C",
          secondary: "#8B4A3C",
          tertiary: "#C4956A",
          highlight: "rgba(139, 74, 60, 0.06)",
          textHighlight: "rgba(139, 74, 60, 0.15)",
        },
        darkMode: {
          light: "#1E1A17",
          lightgray: "#2C2820",
          gray: "#6A6258",
          darkgray: "#C8C0B8",
          dark: "#F5F0E8",
          secondary: "#C4956A",
          tertiary: "#8B4A3C",
          highlight: "rgba(196, 149, 106, 0.1)",
          textHighlight: "rgba(196, 149, 106, 0.2)",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
