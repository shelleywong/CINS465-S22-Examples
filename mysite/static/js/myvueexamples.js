const ListRendering = {
    data() {
        return {
            todos: [
                { text: "Learn JavaScript" },
                { text: "Learn Vue" },
                { text: "Build Something Awesome" }
            ]
        }
    },
}

mylist = Vue.createApp(ListRendering).mount('#list-rendering')

const Counter = {
    data() {
        return {
            count: 0,
            awesome: true
        }
    },
    mounted() {
        setInterval(() => {
            this.count++;
            this.awesome = !this.awesome;
        }, 10000) // every 1 second
    }
}
mycounter = Vue.createApp(Counter).mount('#counter')

Vue.createApp({
    data() {
        return {
            message: 'Hello Vue!'
        }
    }
}).mount('#app')