const QuestRendering = {
    data() {
        return {
            questions: []
        }
    },
    mounted () {
        axios.get('/question_json/')
        .then(function (response) {
            // handle success
            myapp.questions = response.data.questions;
            console.log(response);
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        setInterval(() => {
            axios.get('/question_json/')
            .then(function (response) {
                // handle success
                myapp.questions = response.data.questions;
                console.log(response);
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
        }, 10000);
    }
}

myapp = Vue.createApp(QuestRendering).mount('#quest-rendering')
