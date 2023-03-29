import { useState } from "react"

const Form = () => {
    const [firstName, setFirstName] = useState<string>("")
    const [surname, setSurname] = useState<string>("")
    const [lastName, setLastName] = useState<string>("")
    const [linkedinUser, setLinkedinUser] = useState<string>("")
    const [gitHubUser, setGitHubUser] = useState<string>("")
    const [githubcontribuitions, setGitHubContribuitions] = useState<string>("")
    const [aboutMe, setAboutMe] = useState<string>("")
    const [age, setAge] = useState<string>("")
    const [imageSrc, setImageSrc] = useState<string>("");
    
    interface FormDataType {firstName:string, lastName: string, age: string, aboutMe: string, surname:string, linkedinUser: string, gitHubUser: string, gitHubContribuitions: string}
    const responseBody: FormDataType = {firstName: "", lastName: "", age: "0", aboutMe: "lorem ipsum", surname: "", linkedinUser:"", gitHubUser:"", gitHubContribuitions: ""}

    const onSubmitHandler = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        responseBody.firstName = firstName
        responseBody.lastName = lastName
        responseBody.age = age
        responseBody.aboutMe = aboutMe
        responseBody.surname = surname
        responseBody.linkedinUser = linkedinUser
        responseBody.gitHubUser = gitHubUser
        responseBody.gitHubContribuitions = githubcontribuitions
        console.log(JSON.stringify(responseBody))

    
        try {
            let res = await fetch(`http://127.0.0.1:7000/api/?name=${responseBody.firstName}&surname=${responseBody.surname}&lastname=${responseBody.lastName}&age=${responseBody.age}&aboutme=${responseBody.aboutMe}&githubuser=${responseBody.gitHubUser}&githubcontribuitions=${responseBody.gitHubContribuitions}&linkedinuser=${responseBody.linkedinUser}`, {
              method: "GET"

            });

            if(res.ok)
            {
                let blob = await res.blob();
                let url = URL.createObjectURL(blob);
                setImageSrc(url);
            }
        } catch(err)
        {
            console.log(err);
            
        }
    }

    const inputChangeHandler = (setFunction: React.Dispatch<React.SetStateAction<string>>, event: React.ChangeEvent<HTMLInputElement>) => {
        setFunction(event.target.value)
    }
  

    return (
        <>
            <form onSubmit={onSubmitHandler}>
                <label htmlFor="firstName">first name</label>
                <input type="name" id="firstName" name="firstName" onChange={(e)=>inputChangeHandler(setFirstName, e)} />
                <br></br>
                <label htmlFor="surname">sur name</label>
                <input type="text" id="surname" name="surname" onChange={(e)=>inputChangeHandler(setSurname, e)} />
                <br></br>
                <label htmlFor="lastName">Last name</label>
                <input type="text" id="lastName" name="lastName" onChange={(e)=>inputChangeHandler(setLastName, e)} />
                <br></br> 

                <label htmlFor="Age">Age</label>
                <input type="text" id="Age" name="Age" onChange={(e)=>inputChangeHandler(setAge, e)} />            
                <br></br>

                <label htmlFor="linkedinUser">linkedin user</label>
                <input type="text" id="linkedinUser" name="linkedinUser" onChange={(e)=>inputChangeHandler(setLinkedinUser, e)} />

                <br></br>
                <label htmlFor="gitHubUser">github user</label>
                <input type="text" id="gitHubUser" name="gitHubUser" onChange={(e)=>inputChangeHandler(setGitHubUser, e)} />

                <br></br>

                <label htmlFor="gitHubContribuitions">github contribuitions</label>
                <input type="text" id="gitHubContribuitions" name="gitHubContribuitions" onChange={(e)=>inputChangeHandler(setGitHubContribuitions, e)} />
        
                <br></br>
                <label htmlFor="aboutMe">About me</label>
                <input type="text" id="aboutMe" name="aboutMe" onChange={(e)=>inputChangeHandler(setAboutMe, e)} />

                <br></br>
                <input type="submit" value="Generate Image"/>
            </form>
            <img src={imageSrc} width="200" height="200"></img> 
        </>
    );
}

export default Form;