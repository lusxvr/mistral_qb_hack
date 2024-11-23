<script setup>
import { ScrollArea } from '@/components/ui/scroll-area'
import { useChatLogStore } from '@/pinia/chatLog'
import { ref, watch, nextTick } from 'vue'
import { marked } from 'marked'
import DOMPurify from 'dompurify'

const store = useChatLogStore()
const scrollAreaRef = ref(null)

// DOMPurify configuration
DOMPurify.setConfig({
  ADD_ATTR: ['target', 'rel']
})

// custom renderer for marked
const renderer = {
  link(href, title, text) {
    const link = marked.Renderer.prototype.link.call(this, href, title, text)
    return link.replace('<a', '<a target="_blank" rel="noopener noreferrer"')
  }
}

const renderMarkdown = (text) => {
  // set the renderer options
  marked.setOptions({
    renderer: new marked.Renderer(),
    breaks: true,
    gfm: true
  })

  marked.use({ renderer })

  const html = marked.parse(text)
  const sanitizedHtml = DOMPurify.sanitize(html)
  return sanitizedHtml
}

// scroll to bottom of the chat log after new message is added
const scrollToBottom = () => {
  if (scrollAreaRef.value) {
    const scrollArea = scrollAreaRef.value.$el
    const scrollContent = scrollArea.querySelector('[data-radix-scroll-area-viewport]')
    if (scrollContent) {
      scrollContent.scrollTop = scrollContent.scrollHeight
    }
  }
}

watch(() => store.chatLog.length, () => {
  nextTick(() => {
    scrollToBottom()
  })
})
</script>

<template>
    <ScrollArea ref="scrollAreaRef" class="w-full h-[150px]">
        <div class="min-h-[150px] flex flex-col items-start text-left w-full bg-slate-100 rounded-lg px-4 py-2 space-y-2 [box-shadow:inset_0_2px_4px_0_rgb(0_0_0_/_0.05)]">
            <div v-for="message in [...store.chatLog].sort((a, b) => a.id - b.id)" 
                 :key="message.id" 
                 class="flex flex-row items-start w-full"
            >
                <span class="font-bold w-16 shrink-0">{{ message.user ? 'User:' : 'Agent:' }}</span>
                <span 
                    class="break-words whitespace-normal flex-1 max-w-[80%] prose prose-sm"
                    v-html="renderMarkdown(message.message)"
                ></span>
            </div>
        </div>
    </ScrollArea>
</template>

<style>
/* Basis Markdown Styling */
.prose {
    @apply text-base leading-7;
}
.prose p {
    @apply my-2;
}
.prose ul {
    @apply list-disc list-inside my-2;
}
.prose ol {
    @apply list-decimal list-inside my-2;
}
.prose h1 {
    @apply text-2xl font-bold my-3;
}
.prose h2 {
    @apply text-xl font-bold my-2;
}
.prose h3 {
    @apply text-lg font-bold my-2;
}
.prose code {
    @apply bg-gray-100 px-1 rounded;
}
.prose pre {
    @apply bg-gray-100 p-2 rounded my-2;
}
.prose blockquote {
    @apply border-l-4 border-gray-300 pl-4 my-2;
}
.prose a {
    @apply text-blue-600 hover:underline;
}
</style>