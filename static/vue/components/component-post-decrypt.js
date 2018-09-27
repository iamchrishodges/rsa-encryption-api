Vue.component('component-post-decrypt',
    {
        props:['name', 'head'],
        
            
        data: function(){ 
          return {
            me: '',
            data: {
                encrypted_message: '',         
            },
            resp: {
                message: ''
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
                    this.resp.message = data.message;
                   // this.data.friend_code = '';
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
                        <input v-model="data.encrypted_message" type="text" class="form-control" placeholder="Encrypted Message">
                        </div>
                        <div class="input-group mb-3">
                            <input v-model="resp.message" type="text" class="form-control" placeholder="Message">
                        </div>
                        <a class="btn btn-primary btn-small active" role="button" aria-pressed="true" v-on:click= "submit">Submit</a>
                    </div>
                </div>
            </div>  
        </div>
        `
    }
);