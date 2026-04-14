import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// 所有页面共享的组件
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.ConditionalRender({
    component: Component.Footer({
      links: {
        首页: "/",
      },
    }),
    condition: (page) => page.fileData.slug !== "index",
  }),
}

// 单篇内容页（博客文章、板块页面等）
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    // 首页不显示面包屑
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    // 首页不显示标题（HTML 自定义）
    Component.ConditionalRender({
      component: Component.ArticleTitle(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ConditionalRender({
      component: Component.ContentMeta(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.TagList(),
  ],
  left: [
    Component.ConditionalRender({
      component: Component.PageTitle(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ConditionalRender({
      component: Component.MobileOnly(Component.Spacer()),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ConditionalRender({
      component: Component.Flex({
        components: [
          {
            Component: Component.Search(),
            grow: true,
          },
        ],
      }),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ConditionalRender({
      component: Component.Explorer(),
      condition: (page) => page.fileData.slug !== "index",
    }),
  ],
  // 右侧不显示知识图谱和反向链接
  right: [],
}

// 列表页（标签页、文件夹页）
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        // 深色模式已禁用（本站为固定亮色调设计）
      ],
    }),
    Component.Explorer(),
  ],
  right: [],
}
