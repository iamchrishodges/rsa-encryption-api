Vue.component('component-post-message',
    {
        props:['name', 'head'],
        
            
        data: function(){ 
          return {
            me: '',
            data: {
                message: '',
                friend_code: ''
            }
          }  
        },
        methods:{
            submit: function(event){

                var url = "http://127.0.0.1:5000" + this.name;
                var data = this.data;
                fetch(url, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json; charset=utf-8",
                    },
                    body: JSON.stringify(data), // body data type must match "Content-Type" header
                })
                .then(response => response.json())
                .then((data) => {
                    this.data.message = '';
                    this.data.friend_code = '';
                });             
            }
        }
        ,
        template: `
        <div>
            <div class="card">
                <div class="card-header">
                    {{head}}
                </div>
                <div class="card-body">
                    
                    <div>
                        <div class="input-group mb-3">
                            <input v-model="data.friend_code" type="text" class="form-control" placeholder="Recipient's Friend Code" id="friend-code">
                        </div>
                        <div class="input-group mb-3">
                            <input v-model="data.message" type="text" class="form-control" placeholder="Message" id="message">
                        </div>
                        <a class="btn btn-primary btn-small active" role="button" aria-pressed="true" v-on:click= "submit">Submit</a>
                    </div>
                </div>
            </div>  
        </div>
        `
    }
);